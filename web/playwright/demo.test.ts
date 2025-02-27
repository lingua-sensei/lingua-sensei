import { expect, test } from "@playwright/test";

test("home page has expected h1", async ({ page }) => {
    console.log("hello");
    await page.goto("/");
    console.log("hello 2");
    await expect(page.locator("h1")).toBeVisible();
    console.log("hello 3");
});
