import {Message} from "../models";


export class ChatApi {
    static async postMessage(messages: Message[]): Promise<any> {
        let url = 'http://localhost:8000/'
        let data = {}
        let error = null

        let response = await fetch(
            url,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "messages": messages
                })
            }
        )

        try {
            data = await response.json();
        }
        catch (e: any) {
            error = e.toString()
        }
        let statusCode = response.status

        return {
            statusCode,
            data,
            error,
        }
    }
}