
export enum UserEnum {
    USER = 0,
    AGENT = 1
}

export class User {
    type: UserEnum = UserEnum.USER || UserEnum.AGENT
}

export class Message {
    author: User = new User()
    content: string = ''
}

export class Chat {
    messages: Message[] = []
}