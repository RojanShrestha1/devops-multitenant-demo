from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)

# Simple in-memory "tenant data"
TENANTS = {
    "tenant1": {"name": "Tenant One", "plan": "Free"},
    "tenant2": {"name": "Tenant Two", "plan": "Pro"},
    "tenant3": {"name": "Tenant Three", "plan": "Enterprise"},
}

# Home route
@app.route("/")
def home():
    return "Multi-tenant DevOps Demo is running!"

# Tenant-specific route
@app.route("/tenant/<tenant_id>")
def get_tenant(tenant_id):
    tenant = TENANTS.get(tenant_id)
    if not tenant:
        return jsonify({"error": "Tenant not found"}), 404
    
    return jsonify({
        "tenant_id": tenant_id,
        "data": tenant
    })

if __name__ == "__main__":
    # debug=True helps during development (shows errors)
    app.run(host="0.0.0.0", port=5001, debug=True)
