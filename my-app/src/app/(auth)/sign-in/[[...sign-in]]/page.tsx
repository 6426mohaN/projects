import React from 'react'
import { SignIn} from '@clerk/nextjs'

const SignInPage = () => {
  return (
<main className=' flex w-full h-screen justify-center items-center'>
    <SignIn />
</main>
  )
}

export default SignInPage
