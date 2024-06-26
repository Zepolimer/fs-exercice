

export class ChatApi {
    static async list(messages: Message[]): Promise {
        let url = 'http://localhost:8000/'
        let statusCode = response.status
        let data = {}
        let error = null

        let response = await fetch(
            url,
            {
                method: 'POST',
                json: JSON.stringify({
                    messages
                })
            }
        )

        try {
            data = await response.json();
        }
        catch (e: any) {
            error = e.toString()
        }

        return {
            statusCode,
            data,
            error,
        }
    }
}