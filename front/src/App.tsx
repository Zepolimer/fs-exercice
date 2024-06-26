import React, {useEffect, useRef, useState} from 'react';

import {Chat, Message, User, UserEnum} from "./models";
import {ChatApi} from "./services";
import {MessageFactory} from "./services/factory";


function App() {
    const lastMessage = useRef<null  | HTMLDivElement>(null);

    let user = new User()
    user.type = UserEnum.USER

    let message = new Message()
    message.author = user

    let [userMessage, setUserMessage] = useState<Message>(message)
    let [chat, setChat] = useState<Chat>(new Chat())


    let onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setUserMessage({
            ...userMessage,
            content: event.target.value
        })
    }

    let onClick = () => {
        if (userMessage.content !== '') {
            let chatMessages = [
                ...chat.messages,
                userMessage
            ]
            setChat({
                messages: [
                    ...chat.messages,
                    userMessage
                ]
            })

            ChatApi.postMessage(chatMessages)
                .then((res) => {
                    if (res.statusCode === 201) {
                        let agentMessage = MessageFactory.fromFragment(res.data)
                        setChat({
                            messages: [
                                ...chatMessages,
                                agentMessage
                            ]
                        })
                        setUserMessage(message)
                    }
                })
                .catch((e) => console.error(e))
        }
    }

    useEffect(() => {
        lastMessage!.current!.scrollIntoView({ behavior: "smooth" })
    }, [chat]);


    return (
        <div className={"container mx-auto mt-12 bg-white p-12 rounded-lg shadow-lg"}>
            <div className={'w-full overflow-auto h-[70dvh]'}>
                {
                    chat.messages.length > 0 &&
                    chat.messages.map((message, idx) => {
                        return (
                            <div
                                key={idx}
                                className={'w-full flex flex-col'}
                            >
                                {
                                    message.author.type === UserEnum.USER &&
                                    <div className={'w-1/2 py-3 px-4 bg-blue-100 border border-blue-300 text-lg rounded-md self-end shadow-md'}>
                                        <span className={'font-bold text-blue-300'}>You</span>
                                        <p>{message.content}</p>
                                    </div>
                                }
                                {
                                    message.author.type === UserEnum.AGENT &&
                                    <div className={'w-1/3 py-3 px-4 bg-slate-100 border border-slate-300 text-lg rounded-md self-start shadow-md'}>
                                        <span className={'font-bold text-slate-400'}>Agent</span>
                                        <p>{message.content}</p>
                                    </div>
                                }
                            </div>
                        )
                    })
                }
                <div ref={lastMessage} />
            </div>

            <div className={'w-full mt-12 flex gap-x-4'}>
                <input
                    type={"text"}
                    value={userMessage.content}
                    onChange={onChange}
                    className={"shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"}
                />

                <button
                    onClick={onClick}
                    className={"w-fit bg-teal-400 hover:bg-teal-600 text-white font-bold py-3 px-6 rounded focus:outline-none focus:shadow-outline"}
                >
                    Save
                </button>
            </div>
        </div>
    );
}

export default App;
