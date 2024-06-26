import {MessageFragment} from "./fragments";
import {Message} from "../models";


export class MessageFactory {
    static fromFragment = (fragment: MessageFragment): Message => {
        let message = new Message()
        message.author = fragment.author
        message.content = fragment.content
        return message
    }
}