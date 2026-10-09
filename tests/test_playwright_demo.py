from playwright.sync_api import Page, expect

from Pages.register_page import RegisterPage

def test_register_page(page: Page) -> None:
    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.fill_personal_details()
    register_page.select_gender_and_hobbies()
    register_page.select_languages()
    register_page.select_skill_and_country()
    register_page.upload_sample_file()

    expect(register_page.first_name).to_have_value("Kunal")
    expect(register_page.email).to_have_value("kunal@demo.com")
    expect(register_page.skills).to_have_value("Python")
    expect(register_page.country).to_have_value("India")
    assert (
        register_page.upload_input.evaluate("(input) => input.files[0].name")
        == "sample.txt"
    )
