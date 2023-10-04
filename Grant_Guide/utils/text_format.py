import os
import tempfile

import pypandoc


def convert_markdown_docx(output_text, template_location=None):
    """
    The function `convert_markdown_docx` converts a Markdown document to a DOCX file, optionally using a
    template.

    Args:
      output_text: The `output_text` parameter is the text content that you want to convert from
    Markdown to DOCX format. It should be a string containing the Markdown content.
      template_location: The `template_location` parameter is the file path to a Word document (.docx)
    that will be used as a template for the conversion. If you want to use a specific template for the
    formatting of the converted document, you can provide the file path to the template document. If you
    don't

    Returns:
      the converted DOCX data as a byte string.
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".md", delete=False) as temp_md:
        temp_md.write(output_text)
        temp_md.close()  # It is necessary to close the file before conversion

        with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as temp_docx:
            output_file_name = temp_docx.name  # creating output file name

            if template_location is not None:
                pypandoc.convert_file(
                    temp_md.name,
                    "docx",
                    outputfile=output_file_name,
                    extra_args=["--reference-doc", template_location],
                )  # converting md to docx with template
            else:
                pypandoc.convert_file(
                    temp_md.name, "docx", outputfile=output_file_name
                )  # converting md to docx without template

            temp_docx.seek(0)  # Seek back to the beginning of the file before reading
            docx_data = temp_docx.read()

        # Cleaning up the temporary files
        os.remove(temp_md.name)
        os.remove(output_file_name)

    return docx_data
