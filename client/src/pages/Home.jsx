import { Banner, Button } from 'flowbite-react';
import { HiX } from 'react-icons/hi';
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <Banner className='mt-8'>
      <div className="flex w-[calc(100%-2rem)] flex-col justify-between rounded-lg border border-gray-100 bg-white p-4 shadow-sm dark:border-gray-600 dark:bg-gray-700 md:flex-row lg:max-w-7xl">
        <div className="mb-3 mr-4 flex flex-col items-start md:mb-0 md:flex-row md:items-center">
          <a
            href="https://flowbite.com/"
            className="mb-2 flex items-center border-gray-200 dark:border-gray-600 md:mb-0 md:mr-4 md:border-r md:pr-4"
          >
            <img src="https://flowbite.com/docs/images/logo.svg" className="mr-2 h-6" alt="Flowbite Logo" />
            <span className="self-center whitespace-nowrap text-lg font-semibold dark:text-white md:pr-6">
              Flowbite
            </span>
          </a>
          <p className="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
            Build websites even faster with components on top of Tailwind CSS
          </p>
        </div>
        <div className="flex flex-shrink-0 items-center">
          <Link to="sign-up">
            <Button>
              Sign up
            </Button>              
          </Link>          
        </div>
      </div>
    </Banner>
  );
}
