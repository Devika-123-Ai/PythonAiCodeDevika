const { test, expect } = require('@playwright/test');

test('AWS S3 invalid bucket name', async ({ page }) => {

    // Step 1: Open AWS Console
    await page.goto('https://console.aws.amazon.com/');

    // Step 2: Sign in manually if AWS asks
    // After login, navigate to S3

    // Step 3: Open S3 service
    await page.goto('https://s3.console.aws.amazon.com/s3/home');

    // Step 4: Click Create bucket
    await page
        .getByRole('button', { name: 'Create bucket' })
        .click();

    // Step 5: Enter invalid bucket name
    await page
        .getByLabel('Bucket name')
        .fill('@@@@@@@');

    // Step 6: Verify AWS shows validation error
    await expect(
        page.getByText(/bucket name/i)
    ).toBeVisible();
});