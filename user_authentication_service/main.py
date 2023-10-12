#!/usr/bin/env python3
import requests

URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    requests.post(URL + '/users/', json={"email": email, "password": password})


def log_in_wrong_password(email: str, password: str) -> None:
    requests.post(URL + '/sessions/', json={"email": email, "password": password + "p"})


def log_in(email: str, password: str) -> str:
    RESULT = requests.post(URL + '/sessions/', json={"email": email, "password": password})

    return RESULT.cookies.get("session_id")


def profile_unlogged() -> None:
    requests.get(URL + '/profiles/')


def profile_logged(session_id: str) -> None:
    requests.get(URL + '/profiles/', cookies={"session_id": session_id})


def log_out(session_id: str) -> None:
    requests.delete(URL + '/sessions/', cookies={"session_id": session_id})


def reset_password_token(email: str) -> str:
    RESPONSE = requests.post(URL + '/reset_password/', json={"email": email})

    return RESPONSE.cookies.get("reset_token")

def update_password(email: str, reset_token: str, new_password: str) -> None:
    requests.put(
        URL + '/reset_password/',
        json={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
        }
    )


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
