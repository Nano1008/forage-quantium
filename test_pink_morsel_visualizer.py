from daily_sales_data_pink_morsels import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#app-header", timeout=10)

def test_visualisation_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=10)

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radioitems", timeout=10)