import { expect, test } from '@playwright/test';

test.describe('invalid login', async () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('get title', async ({ page }) => {
    expect(page.getByText(/Login form/)).toBeTruthy();
  });

  test('valid login', async ({ page }) => {
    await page.getByRole('textbox', { name: /username/i }).fill('nori');
    await page.getByRole('textbox', { name: /password/i }).fill('password');
    await page.getByRole('button', { name: /submit/i }).click();

    await expect(page.getByText('Hello, nori!')).toBeVisible();
  });

  test('wrong password', async ({ page }) => {
    await page.getByRole('textbox', { name: /username/i }).fill('nori');
    await page.getByRole('textbox', { name: /password/i }).fill('password_');
    await page.getByRole('button', { name: /submit/i }).click();

    await expect(page.getByText(/Invalid username\/password/)).toBeVisible();
  });

  test('wrong username', async ({ page }) => {
    await page.getByRole('textbox', { name: /username/i }).fill('nori_');
    await page.getByRole('textbox', { name: /password/i }).fill('password');
    await page.getByRole('button', { name: /submit/i }).click();

    await expect(page.getByText(/Invalid username\/password/)).toBeVisible();
  });

  test('input nothing', async ({ page }) => {
    await page.getByRole('button', { name: /submit/i }).click();

    await expect(page.getByText(/Invalid username\/password/)).toBeVisible();
  });
});
