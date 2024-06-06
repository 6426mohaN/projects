import { useUser } from '@clerk/nextjs';
import {StreamVideoClient,StreamVideo,User,
  } from '@stream-io/video-react-sdk';
import { ReactNode, useEffect, useState } from 'react';
import { tokenProvider } from '../actions/stream.actions';
  
  const apiKey = process.env.NEXT_PUBLIC_STREAM_API_KEY;


  
  const StreamVideoProvider= ({children}: {children: ReactNode}) => {
      const [videoClient, setVideoClient] = useState<StreamVideoClient>();
        const {user, isLoaded } = useUser()

      useEffect(()=>{
        if(!isLoaded || !user) return;
        if(!apiKey) throw new Error('Stream API key missing')

            const client = new StreamVideoClient({
                apiKey,
                user: {
                    id: user?.id,
                    name: user?.username || user?.id,
                    image: user?.imageUrl,
                },
                tokenProvider,

            })
            setVideoClient(client)
    
    }, [user, isLoaded]);
    if(!videoClient) return

    return (
      <StreamVideo client={videoClient}>

      </StreamVideo>
    );
  };
  export default StreamVideoProvider;