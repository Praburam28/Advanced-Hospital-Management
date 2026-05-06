from fastapi import HTTPException

def role_required(required_roles):

    def checker(user_role):

        if user_role not in required_roles:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

    return checker