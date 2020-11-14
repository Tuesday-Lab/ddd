from rest_framework import status


def test_미로그인유저_이벤트_생성_403_응답(client):
    response = client.post('/v1/events/')
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_어드민유저_이벤트_생성(auto_login_user):
    client, user = auto_login_user(is_admin=True)
    client.login(user=user)
    data = {
        "title": "Event",
        "slug": "slug",
        "kind": "NORMAL",
        "amount": 1000.00,
        "currency": "KRW",
        "max_attendee_count": 1,
        "description": "Event Test",
    }
    response = client.post('/v1/events/', data=data)

    assert response.status_code == status.HTTP_200_OK
