
export enum UserEnum {
    USER = 0
    AGENT = 1
}

export interface Identifier {
    id: str
}

export class User implements Identifier {
    id: str = ''
    type: UserEnum = UserEnum.USER || UserEnum.AGENT
}

export class Message implements Identifier {
    id: str = ''
    author: User = new User()
    content: str = ''
}

export class Chat implements Identifier {
    id: str = ''
    messages: Message[] = []
}