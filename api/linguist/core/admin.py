from django.contrib import admin
from linguist.core.models import Audio
from django.db.models import Count
from django.utils.html import format_html
from django.db.models import Q


class SentenceWordFilter(admin.SimpleListFilter):
    title = 'audio type'
    parameter_name = 'is_sentence'

    def lookups(self, request, model_admin):
        return (
            ('sentence', 'Sentence'),
            ('word', 'Word'),
        )

    def queryset(self, request, queryset):
        queryset = queryset.annotate(linked_count=Count('linked_audios'))

        if self.value() == 'sentence':
            return queryset.filter(
                Q(linked_count__gt=0) &
                ~Q(correspondent_text__isnull=True) &
                ~Q(correspondent_text='') &
                ~Q(correspondent_language__isnull=True) &
                ~Q(correspondent_language='') &
                Q(text__contains=' ')
            )
        elif self.value() == 'word':
            return queryset.filter(
                Q(linked_count=0) |
                Q(correspondent_text__isnull=True) |
                Q(correspondent_text='') |
                Q(correspondent_language__isnull=True) |
                Q(correspondent_language='') |
                ~Q(text__contains=' ')
            )
        return queryset

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('text', 'audio_player', 'language', 'created_at', 'updated_at', 'is_sentence')
    list_filter = ('language', 'created_at', 'updated_at', SentenceWordFilter)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('text', 'correspondent_text')
    date_hierarchy = 'created_at'
    filter_horizontal = ['linked_audios']
    ordering = ('updated_at', 'language')

    def audio_player(self, obj):
        if obj.file:
            return format_html(
                '<audio controls><source src="{}" type="audio/mpeg">Your browser does not support the audio element.</audio>',
                obj.file.url
            )
        return "No audio file"

    audio_player.short_description = 'Audio'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name != "linked_audios":
            return super().formfield_for_manytomany(db_field, request, **kwargs)

        manager = Audio.objects
        object_id = request.resolver_match.kwargs.get('object_id')

        if object_id:
            manager = manager.exclude(id=object_id)

        kwargs["queryset"] = manager.exclude(text__contains=' ')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            linked_audio_count=Count('linked_audios')
        )
        return queryset

    def is_sentence(self, obj):
        has_links = obj.linked_audio_count > 0
        has_correspondent_info = bool(obj.correspondent_text and obj.correspondent_language)
        is_not_single_word = ' ' in (obj.text or '')
        return has_links and has_correspondent_info and is_not_single_word

    is_sentence.boolean = True
    is_sentence.admin_order_field = 'linked_audio_count'
    is_sentence.short_description = 'Sentence'
