class RBACSystem:
    def __init__(self):
        # Define roles and their fixed permissions for the "Account" object
        self.role_permissions = {
            "Admin": ["Create", "View", "Update", "Delete"],
            "Manager": ["View", "Update"],
            "Customer": ["View"]
        }
        # Mapping users to their assigned roles
        self.user_roles = {}

    def assign_role_to_user(self, username, role):
        if role in self.role_permissions:
            self.user_roles[username] = role
            print(f"[SUCCESS] User '{username}' successfully assigned to role '{role}'.")
        else:
            print(f"[ERROR] Role '{role}' does not exist.")

    def check_permission(self, username, action):
        if username not in self.user_roles:
            print(f"[ACCESS DENIED] User '{username}' is not registered in the system.")
            return False
        
        user_role = self.user_roles[username]
        allowed_permissions = self.role_permissions[user_role]
        
        if action in allowed_permissions:
            print(f"[ACCESS GRANTED] User '{username}' (Role: {user_role}) is PERMITTED to perform action: '{action}'.")
            return True
        else:
            print(f"[ACCESS DENIED] User '{username}' (Role: {user_role}) is DENIED to perform action: '{action}'.")
            return False

# --- Execution Demonstration / Test Case ---
if __name__ == "__main__":
    print("=== Role-Based Access Control (RBAC) Simulation ===")
    rbac = RBACSystem()

    # 1. Assigning users to roles
    rbac.assign_role_to_user("Alice", "Admin")
    rbac.assign_role_to_user("Bob", "Manager")
    rbac.assign_role_to_user("Charlie", "Customer")

    print("\n--- Testing Permissions ---")
    # Admin tests
    rbac.check_permission("Alice", "Delete")
    rbac.check_permission("Alice", "View")

    # Manager tests
    rbac.check_permission("Bob", "Update")
    rbac.check_permission("Bob", "Create")  # Should fail

    # Customer tests
    rbac.check_permission("Charlie", "View")
    rbac.check_permission("Charlie", "Update")  # Should fail