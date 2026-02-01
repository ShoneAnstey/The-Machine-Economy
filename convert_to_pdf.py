import markdown
from xhtml2pdf import pisa

def convert_md_to_pdf(source_md, output_pdf):
    # 1. Read Markdown file
    with open(source_md, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Convert Markdown to HTML
    html_content = markdown.markdown(text, extensions=['extra', 'tables', 'toc'])

    # 3. Add styling (CSS) for a professional whitepaper look
    full_html = f"""
    <html>
    <head>
    <style>
        @page {{
            size: letter;
            margin: 2.5cm;
            @frame footer_frame {{
                -pdf-frame-content: footerContent;
                bottom: 1cm;
                margin-left: 1cm;
                margin-right: 1cm;
                height: 1cm;
            }}
        }}
        
        body {{
            font-family: Helvetica, Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #333333;
        }}
        
        h1 {{
            font-size: 24pt;
            color: #111111;
            border-bottom: 2px solid #333333;
            padding-bottom: 10px;
            margin-top: 0;
            margin-bottom: 20px;
        }}
        
        h2 {{
            font-size: 18pt;
            color: #222222;
            margin-top: 30px;
            margin-bottom: 10px;
            border-bottom: 1px solid #eeeeee;
        }}
        
        h3 {{
            font-size: 14pt;
            color: #444444;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        p {{
            margin-bottom: 10px;
            text-align: justify;
        }}
        
        li {{
            margin-bottom: 5px;
        }}
        
        code {{
            font-family: Courier, monospace;
            background-color: #f5f5f5;
            padding: 2px;
        }}
        
        pre {{
            background-color: #f5f5f5;
            padding: 10px;
            border: 1px solid #dddddd;
        }}

        blockquote {{
            border-left: 4px solid #dddddd;
            padding-left: 10px;
            margin-left: 20px;
            color: #555555;
            font-style: italic;
        }}
        
        /* Specific tweaks for this document */
        .meta {{
            font-size: 10pt;
            color: #666666;
            margin-bottom: 30px;
        }}
        
        #footerContent {{
            text-align: center;
            color: #888888;
            font-size: 8pt;
        }}
    </style>
    </head>
    <body>
        {html_content}
        
        <div id="footerContent">
            The Machine Economy - Whitepaper<br>
            <pdf:pagenumber>
        </div>
    </body>
    </html>
    """

    # 4. Write PDF
    with open(output_pdf, "wb") as result_file:
        pisa_status = pisa.CreatePDF(
            full_html,
            dest=result_file
        )

    if pisa_status.err:
        print(f"Error generating PDF: {pisa_status.err}")
    else:
        print(f"Successfully created: {output_pdf}")

if __name__ == "__main__":
    convert_md_to_pdf("AI_Agents_and_the_Lightning_Network.md", "AI_Agents_and_the_Lightning_Network.pdf")
