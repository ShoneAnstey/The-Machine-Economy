import markdown
from xhtml2pdf import pisa
import os

def convert_md_to_pdf(source_md, output_pdf):
    # 1. Read Markdown file
    with open(source_md, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Convert Markdown to HTML
    html_content = markdown.markdown(text, extensions=['extra', 'tables', 'toc'])

    # 3. Add Professional Whitepaper Styling
    full_html = f"""
    <html>
    <head>
    <style>
        @page {{
            size: letter;
            margin: 2.5cm;
            @frame header_frame {{
                -pdf-frame-content: headerContent;
                top: 1cm;
                margin-left: 2.5cm;
                margin-right: 2.5cm;
                height: 1cm;
            }}
            @frame footer_frame {{
                -pdf-frame-content: footerContent;
                bottom: 1cm;
                margin-left: 2.5cm;
                margin-right: 2.5cm;
                height: 1cm;
            }}
        }}

        /* 3. Font Pairing (Serif Body, Sans Header) */
        body {{
            font-family: "Times New Roman", Times, serif;
            font-size: 11pt;
            line-height: 1.25; /* 2. Increase line spacing */
            color: #222222;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: Helvetica, Arial, sans-serif;
            color: #111111;
            font-weight: normal; /* Lighter weight perception */
        }}

        /* 1. Title Page Improvements */
        h1 {{
            font-size: 26pt;
            line-height: 1.2;
            margin-top: 2cm;
            margin-bottom: 0.5cm;
            text-align: left;
            border-bottom: none;
        }}
        
        /* Subtitle (Italic text following H1) */
        em {{
            font-family: Helvetica, Arial, sans-serif;
            font-size: 14pt;
            color: #555555;
            display: block;
            margin-bottom: 2cm; /* Vertical spacing before abstract */
            font-style: normal;
            font-weight: 300;
        }}

        /* 4. Spacing between sections */
        h2 {{
            font-size: 16pt;
            margin-top: 30px; /* Space before section */
            margin-bottom: 15px;
            padding-top: 10px;
            border-top: 1px solid #eeeeee; /* Minimal divider above section */
            border-bottom: none;
        }}

        h3 {{
            font-size: 12pt;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #444444;
        }}

        /* 5. List improvements */
        ul, ol {{
            margin-top: 5px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px; /* Vertical spacing between bullets */
            font-size: 10.5pt; /* Slightly smaller than body */
            line-height: 1.4;
        }}

        p {{
            margin-bottom: 12px;
            text-align: justify;
        }}

        code {{
            font-family: Courier, monospace;
            background-color: #f5f5f5;
            padding: 1px 3px;
        }}
        
        blockquote {{
            border-left: 3px solid #ccc;
            padding-left: 10px;
            margin: 20px 0 20px 20px;
            font-style: italic;
            color: #555;
        }}
        
        /* Header/Footer Polish */
        #headerContent {{
            text-align: right;
            color: #999999;
            font-family: Helvetica, Arial, sans-serif;
            font-size: 8pt;
        }}
        
        #footerContent {{
            text-align: center;
            color: #999999;
            font-family: Helvetica, Arial, sans-serif;
            font-size: 9pt;
        }}
    </style>
    </head>
    <body>
        <div id="headerContent">
            The Machine Economy — White Paper
        </div>

        {html_content}
        
        <div id="footerContent">
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
