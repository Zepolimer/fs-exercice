

export interface MessageFragment {
    id: string
    author: {
        id: string,
        type: number
    },
    content: string
}