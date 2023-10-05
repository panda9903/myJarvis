import requests


class BardAPI:
    def _init_(self, psid):
        self.psid = psid
        # Replace the URL with the actual Bard API endpoint
        self.api_url = "https://bard.google.com/chat"

    def get_answer(self, question):
        headers = {
            "__Secure-1PSID": self.psid,
            "Content-Type": "application/json",
        }

        params = {
            "question": question,
        }

        response = requests.get(self.api_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Request failed with status code: " +
                            str(response.status_code))


# Replace 'YOUR_PSID' with your actual "__Secure-1PSID" value
psid = 'bghj1aB6sa0mAe7Mkuh3GT47o2QhDPsRJWOqzPacQtDc1ux2URVcetWMQ32yA-eku6L4hA.'
question = 'what is 2+2'

try:
    bard_api = BardAPI(psid)
    response = bard_api.get_answer(question)
    print(response)
except Exception as e:
    print("Error:", e)
