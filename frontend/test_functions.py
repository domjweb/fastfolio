"""
Simple test to verify Azure Function implementations work correctly.
This can be used to test the functions before deployment.
"""
import sys
import json
from unittest.mock import MagicMock
sys.path.append('.')

# Mock Azure Functions
class MockHttpRequest:
    def __init__(self, method="GET", body=None):
        self.method = method
        self._body = body
    
    def get_json(self):
        return json.loads(self._body) if self._body else None

class MockHttpResponse:
    def __init__(self, body, status_code=200, headers=None):
        self.body = body
        self.status_code = status_code
        self.headers = headers or {}

# Test functions
def test_function(function_path, request=None):
    """Test a function and return the response"""
    import importlib.util
    
    # Load the function module
    spec = importlib.util.spec_from_file_location("function", function_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["azure.functions"] = MagicMock()
    
    # Mock the func module
    mock_func = MagicMock()
    mock_func.HttpRequest = MockHttpRequest
    mock_func.HttpResponse = MockHttpResponse
    sys.modules["azure.functions"] = mock_func
    
    spec.loader.exec_module(module)
    
    # Create a test request
    if request is None:
        request = MockHttpRequest()
    
    # Call the main function
    response = module.main(request)
    return response

if __name__ == "__main__":
    print("🧪 Testing Azure Functions locally...")
    
    # Test about endpoint
    print("\n📋 Testing /api/about endpoint:")
    try:
        response = test_function("api/about/__init__.py")
        print(f"Status: {response.status_code}")
        print(f"Body: {response.body[:200]}...")
        if response.status_code == 200:
            data = json.loads(response.body)
            print(f"✅ About endpoint working - Name: {data.get('name', 'N/A')}")
    except Exception as e:
        print(f"❌ About endpoint failed: {e}")
    
    # Test experiences endpoint
    print("\n💼 Testing /api/experiences endpoint:")
    try:
        response = test_function("api/experiences/__init__.py")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = json.loads(response.body)
            exp_count = len(data.get('experiences', []))
            print(f"✅ Experiences endpoint working - Found {exp_count} experiences")
    except Exception as e:
        print(f"❌ Experiences endpoint failed: {e}")
    
    # Test contact GET
    print("\n📞 Testing /api/contact GET endpoint:")
    try:
        response = test_function("api/contact/__init__.py", MockHttpRequest("GET"))
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = json.loads(response.body)
            print(f"✅ Contact GET working - Email: {data.get('email', 'N/A')}")
    except Exception as e:
        print(f"❌ Contact GET failed: {e}")
    
    # Test contact POST
    print("\n📧 Testing /api/contact POST endpoint:")
    try:
        test_data = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test Subject",
            "message": "Test message"
        }
        request = MockHttpRequest("POST", json.dumps(test_data))
        response = test_function("api/contact/__init__.py", request)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = json.loads(response.body)
            print(f"✅ Contact POST working - Message: {data.get('message', 'N/A')}")
    except Exception as e:
        print(f"❌ Contact POST failed: {e}")
    
    print("\n🎉 Local testing complete!")