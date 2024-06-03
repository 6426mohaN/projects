import React, { Children, ReactNode } from 'react'

const RootLayout = ({children}:{children:ReactNode}/**childeren is a react props using typescript*/) => {
  return (
    <main>
        {children}
    </main>
  )
}

export default RootLayout
