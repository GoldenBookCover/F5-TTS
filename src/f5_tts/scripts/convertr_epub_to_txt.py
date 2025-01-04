"""
Convert epub files to txt files
pip install ebooklib beautifulsoup4
Get-ChildItem .\*.epub | % { python .\src\f5_tts\scripts\convertr_epub_to_txt.py $_.FullName $_.FullName.Replace('.epub', '-txt') }

TODO
convertr_epub_to_txt.py:1: SyntaxWarning: invalid escape sequence '\*'
Converting E:\projects\F5-TTS\data\सत्यताको पछ्याइमा – १.epub
site-packages\ebooklib\epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
site-packages\ebooklib\epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
"""

import os
import sys
try :
    from ebooklib import epub
    from bs4 import BeautifulSoup
except ImportError :
    print('Module not found, try installing:')
    print('pip install ebooklib beautifulsoup4')
    sys.exit(4)


def epub_to_text(epub_file, output_dir):
    # Load the EPUB file
    print(f"Converting {epub_file}")
    book = epub.read_epub(epub_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chapter_count = 0

    for item in book.get_items():
        # Check if the item is a document (usually XHTML)
        if item.media_type == 'application/xhtml+xml':
            chapter_count += 1
            # Extract content and clean up HTML
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text(separator='\n')

            # Create a .txt file for each chapter
            output_file = os.path.join(output_dir, f'chapter_{chapter_count:04}.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)

            print(f"Extracted: {output_file}")

    print(f"Conversion complete. {chapter_count} chapters extracted.")


if __name__ == "__main__":
    epub_to_text(sys.argv[1], sys.argv[2])
