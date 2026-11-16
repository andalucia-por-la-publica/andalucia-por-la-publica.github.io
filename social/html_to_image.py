"""
Script para convertir HTMLs a imágenes JPEG
Requiere: pip install playwright pillow
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

async def html_to_image(html_file, output_file):
    """Convierte un HTML a imagen JPEG"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})

        # Cargar el archivo HTML
        file_path = f"file://{os.path.abspath(html_file)}"
        await page.goto(file_path, wait_until="networkidle")

        # Capturar como imagen
        await page.screenshot(path=output_file, full_page=True)
        await browser.close()

        print(f"✅ Generado: {output_file}")

async def main():
    """Convierte todos los HTMLs a JPEGs"""
    html_files = [
        ("social-infantil.html", "social-infantil.jpeg"),
        ("social-primaria.html", "social-primaria.jpeg"),
        ("social-secundaria.html", "social-secundaria.jpeg"),
        ("social-universidad.html", "social-universidad.jpeg"),
        ("social-pas.html", "social-pas.jpeg"),
    ]

    print("Convirtiendo HTMLs a imágenes JPEG...")
    print("=" * 50)

    for html_file, output_file in html_files:
        if os.path.exists(html_file):
            try:
                await html_to_image(html_file, output_file)
            except Exception as e:
                print(f"❌ Error con {html_file}: {e}")
        else:
            print(f"⚠️  No encontrado: {html_file}")

    print("=" * 50)
    print("¡Listo! Las imágenes están generadas.")

if __name__ == "__main__":
    asyncio.run(main())
