from pathlib import Path
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parent
for pdf in sorted((ROOT/'final_pdf').glob('*.pdf')):
    dest=ROOT/'final_qa'/pdf.stem
    if list(dest.glob('page-*.png')):continue
    dest.mkdir(parents=True,exist_ok=True)
    d=pdfium.PdfDocument(pdf)
    for i in range(len(d)):d[i].render(scale=1.6).to_pil().save(dest/f'page-{i+1}.png')
    print(pdf.stem,len(d),flush=True)
