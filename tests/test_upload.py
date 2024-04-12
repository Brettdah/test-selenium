"""Module providing test fonctions to upload a file in different scenario."""

from seleniumbase import BaseCase


class UploadTest(BaseCase):

    """Class to use for the upload manipulation"""

    def test_visible_upload(self):

        """Function Uploading a file via a visible file input."""

        # Open home page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = "./data/HK47_love.jpg"
        # upload file
        self.choose_file("#file-upload", file_path)
        self.click("#file-submit")

        # assert file upload text
        self.assert_text("File Uploaded!", "h3")

    def test_hidden_upload(self):

        """Function Uploading a file via an hidden file input."""

        # Open home page
        self.open("https://practice.sdetunicorns.com/cart/")
        # or from home click the cart...

        # get file path
        file_path = "./data/HK47_love.jpg"
        # js code to remove the class *hidden_file*
        rm_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(rm_class)

        # upload file
        self.choose_file("#upfile_1", file_path)
        self.click("#upload_1")

        # assert file upload text
        self.assert_text(
            "File HK47_love.jpg uploaded successfully",
            "#wfu_messageblock_header_1_label_1"
        )
