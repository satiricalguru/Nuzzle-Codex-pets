from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
    errors = []
    missing = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: errors.append(str(exc)))
    page.on("response", lambda response: missing.append(response.url) if response.status == 404 else None)
    
    print("Navigating to Nuzzle local server...")
    page.goto("http://127.0.0.1:4173", wait_until="networkidle")

    # 1. Title & Header Verification
    assert page.title() == "Nuzzle — your agents, with a little more life"
    assert page.locator("#activity-list .activity-item").count() >= 4
    assert page.locator("#pet-strip .pet-tile").count() == 4
    assert page.locator("#hero-pet-name").inner_text() == "Hu Tao"

    # 2. Interactive Petting & Animation Engine Verification
    print("Testing pet interaction...")
    page.locator("#pet-me-button").click()
    assert "state-pat" in page.locator("#hero-pet-art").get_attribute("class")
    page.wait_for_timeout(300)
    assert page.locator(".toast").count() >= 1

    # 3. Simulate Live Agent Event
    print("Testing agent event simulation...")
    prev_count = page.locator("#activity-list .activity-item").count()
    page.locator("#simulate-event-button").click()
    assert page.locator("#activity-list .activity-item").count() == prev_count + 1

    # 4. Companion Switching from Pet Strip
    print("Testing pet strip selection...")
    page.locator("#pet-strip .pet-tile[data-pet-id='furina']").click()
    assert page.locator("#hero-pet-name").inner_text() == "Furina"

    # 5. Pet Library View, Search & Filtering
    print("Testing Pet Library...")
    page.get_by_role("button", name="Pet library").click()
    assert page.locator("#library-view").is_visible()
    assert page.locator("#library-grid .library-card").count() == 8

    page.locator("#pet-search").fill("Klee")
    assert page.locator("#library-grid .library-card").count() == 1
    
    # Select Klee from library
    page.locator(".library-select-btn").click()
    page.get_by_role("button", name="Overview").click()
    assert page.locator("#hero-pet-name").inner_text() == "Klee"

    # 6. Agents View & Toggles
    print("Testing Agents View...")
    page.get_by_role("button", name="Agents").click()
    assert page.locator("#agent-grid .agent-card").count() == 6
    page.locator("#agent-grid .agent-card .toggle").first.click()

    # 7. Settings View & Sub-Tabs
    print("Testing Settings Sub-Tabs...")
    page.get_by_role("button", name="Settings").click()
    assert page.locator("#settings-panel-appearance").is_visible()
    
    # Switch to behavior tab
    page.locator(".settings-tab[data-settings-tab='behavior']").click()
    assert page.locator("#settings-panel-behavior").is_visible()

    # Switch to sound tab
    page.locator(".settings-tab[data-settings-tab='sound']").click()
    assert page.locator("#settings-panel-sound").is_visible()

    # Switch to privacy tab
    page.locator(".settings-tab[data-settings-tab='privacy']").click()
    assert page.locator("#settings-panel-privacy").is_visible()

    # 8. Command Palette (⌘ K) & Search
    print("Testing Command Palette...")
    page.keyboard.press("Meta+K")
    assert page.locator("#command-palette.open").count() == 1
    page.locator("#palette-input").fill("Raiden")
    assert page.locator(".palette-item").count() >= 1
    page.keyboard.press("Escape")
    assert page.locator("#command-palette.open").count() == 0

    # Capture visual verification artifact
    screenshot_path = "/tmp/nuzzle-verify.png"
    page.get_by_role("button", name="Overview").click()
    page.screenshot(path=screenshot_path, full_page=True)
    
    print({
        "status": "ALL_TESTS_PASSED",
        "console_errors": errors,
        "missing_404s": missing,
        "screenshot": screenshot_path
    })
    browser.close()
