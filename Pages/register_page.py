from playwright.sync_api import Locator, Page


class RegisterPage:
    URL = "https://demo.automationtesting.in/Register.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name: Locator = page.get_by_placeholder("First Name")
        self.email: Locator = page.locator("input[ng-model='EmailAdress']")
        self.skills: Locator = page.locator("#Skills")
        self.country: Locator = page.locator("#country")
        self.upload_input: Locator = page.locator("#imagesrc")

    def navigate(self) -> None:
        self.page.goto(self.URL)

    def fill_personal_details(self) -> None:
        self.first_name.fill("Kunal")
        self.page.get_by_placeholder("Last Name").fill("Shah")
        self.page.locator("textarea[ng-model='Adress']").fill(
            "Pune, Maharashtra, India"
        )
        self.email.fill("kunal@demo.com")
        self.page.locator("input[ng-model='Phone']").fill("9876543210")

    def select_gender_and_hobbies(self) -> None:
        self.page.get_by_role("radio", name="Male", exact=True).check()
        self.page.locator("input[type='checkbox'][value='Movies']").check()
        self.page.locator("input[type='checkbox'][value='Hockey']").check()

    def select_languages(self) -> None:
        self.page.locator("#msdd").click()
        self.page.get_by_text("English", exact=True).click()
        self.page.get_by_text("Spanish", exact=True).click()
        self.page.get_by_text("Automation Demo Site").click()

    def select_skill_and_country(self) -> None:
        self.skills.select_option("Python")
        self.page.locator("span[role='combobox']").click()
        self.page.locator("input[role='textbox']").fill("India")
        self.page.locator("li:has-text('India')").click()

    def upload_sample_file(self) -> None:
        self.upload_input.set_input_files(
            {
                "name": "sample.txt",
                "mimeType": "text/plain",
                "buffer": b"sample upload",
            }
        )
