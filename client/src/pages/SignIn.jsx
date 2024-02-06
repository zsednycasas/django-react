import { Button, Card, Checkbox, Label, TextInput } from 'flowbite-react';

export default function SignIn() {
  return (
    <div className='flex-1 gap-5 flex items-center justify-center mt-8'>
      <Card className="w-full max-w-md">
        <form className="flex flex-col gap-4">
          <div>
            <div className="mb-2 block">
              <Label htmlFor="email1" value="Your email" />
            </div>
            <TextInput id="email1" type="email" placeholder="name@flowbite.com" required />
          </div>
          <div>
            <div className="mb-2 block">
              <Label htmlFor="password1" value="Your password" />
            </div>
            <TextInput id="password1" type="password" required />
          </div>
          <div className="flex items-center gap-2">
            <Checkbox id="remember" />
            <Label htmlFor="remember">Remember me</Label>
          </div>
          <Button gradientDuoTone="pinkToOrange">Sign In</Button>
        </form>
      </Card>
    </div>
  );
}
