from locust import HttpUser, task, between

class AttendanceUser(HttpUser):
    wait_time = between(1, 2)  # random delay

    @task
    def send_attendance(self):
        payload = {
            "device_id": "Rabby_pukpuk",
            "message": "CARD123456",
            "signature": "test_signature"
        }
        self.client.post("http://127.0.0.1:1013/attendance", json=payload)
