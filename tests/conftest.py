import io
import os
import pytest
import logging
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="session", autouse=True)
def browser_setup():
    pass

@pytest.fixture(scope="session", autouse=True)
def page(request):

    worker_id = os.environ.get("PYTEST_XDIST_WORKER", "master")

    screenshot_dir = f"artifact/{worker_id}/screenshots"
    video_dir = f"artifact/{worker_id}/videos"
    trace_dir = f"artifact/{worker_id}/traces"

    os.makedirs(screenshot_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(trace_dir, exist_ok=True)
    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    with sync_playwright() as playwright:
        # Launch the chrome browser in non-headless mode 
        browser = playwright.chromium.launch(headless=False) 
        # Create an isolated browser context for the test
        context = browser.new_context(
            record_video_dir="videos/",  # Directory to save video recordings
            record_video_size={"width": 1280, "height": 720}  # Set the video resolution
        )
        # Enable the Trace Viewer for debugging
        # context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # Create a new page in the browser context
        page = context.new_page()
        # return the page object to the test function
        yield page
        # Stop tracing and save the trace to a file
        # context.tracing.stop(path="trace.zip")
        # Trace only on test case failure
        # if request.node.rep_call.failed:
        #     context.tracing.stop(path="trace.zip")
        # After the test is done, close the browser context and the browser
        context.close()
        browser.close()

