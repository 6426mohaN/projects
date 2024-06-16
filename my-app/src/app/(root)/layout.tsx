'use client'//remove if necessary but it requires it due to useEffect on StreamclientProvider.tsx
import React, { ReactNode } from 'react'
import StreamVideoProvider from '../../../providers/StreamClientProvider'

const RootLayout = ({children}:{children:ReactNode}/**childeren is a react props using typescript*/) => {
  return (
    <main>
      <StreamVideoProvider>
        {children}
      </StreamVideoProvider>
    </main>
  )
}

export default RootLayout
