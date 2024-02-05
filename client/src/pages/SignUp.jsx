import { Alert, Button, Label, Spinner, TextInput } from "flowbite-react";
import { HiInformationCircle } from 'react-icons/hi';
import { useState } from "react";
import { Link } from "react-router-dom";

export default function SignUp() {
    const [formData, setFormData] = useState({});
    const [errorMessage, setErrorMessage] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);
    const [loading, setLoading] = useState(false);
    
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.id]: e.target.value.trim() });
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        if(!formData.student_id || !formData.first_name || !formData.middle_name || !formData.last_name || !formData.address || !formData.contact || !formData.username || !formData.password){
            return setErrorMessage('Please fill the blank fields.');
        }
        try {
            setLoading(true);
            setErrorMessage(null);
            setSuccessMessage(null);

            const res = await fetch("/api/create-student/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData),
            });
        
            if (!res.ok) {
                // Check if the response status is not in the range [200, 299]
                const errorData = await res.json();
                return setErrorMessage(errorData.message);
            }
        
            const data = await res.json();
            
            if (data.success === false) {
                return setErrorMessage(data.message);
            } 
            setSuccessMessage(data.message); // Set success message
            setFormData({
                student_id: '', first_name: '', middle_name: '', last_name: '', address: '', contact: '', username: '', password: ''
            });
            setLoading(false);
        } catch (error) {
            setErrorMessage(error.message);
        } finally {
            setLoading(false);
        }       
    };
  return <div className='min-h-screen mt-10'>
    <div className="flex p-3 max-w-5xl mx-auto flex-col md:flex-row md:items-top gap-5">
        
        {/* {left} */}
        <div className="flex-1">
            <Link
             to="/" className="font-semibold dark:text-white text-4xl"> 
                <span className="px-2 py-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-lg text-white text-4xl">Zsedny</span>    
                Vlog
            </Link> 
            <p className="text-sm mt-5">
                This is a demo project using django and react. You can sign up with your email and password or with Google.
            </p> 
        </div>

        {/* {right} */}
        <div className="flex-1">
                {
                    (errorMessage || successMessage) && (
                        <Alert className="mt-5" color={errorMessage ? "failure" : "success"} icon={HiInformationCircle}>
                            {errorMessage || successMessage}
                        </Alert>
                    )
                }
                <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
                <div>
                    <Label value="Your id" />
                    <TextInput type="text" placeholder="Student ID" value={formData.student_id} onChange={handleChange} id="student_id" />
                </div>
                <div>
                    <Label value="Your first name" />
                    <TextInput type="text" placeholder="First name" value={formData.first_name} onChange={handleChange} id="first_name" />
                </div>
                <div>
                    <Label value="Your middle name" />
                    <TextInput type="text" placeholder="Middle name" value={formData.middle_name} onChange={handleChange} id="middle_name" />
                </div>
                <div>
                    <Label value="Your last name" />
                    <TextInput type="text" placeholder="Last name" value={formData.last_name} onChange={handleChange} id="last_name" />
                </div>
                <div>
                    <Label value="Your address" />
                    <TextInput type="text" placeholder="Address" value={formData.address} onChange={handleChange} id="address" />
                </div>
                <div>
                    <Label value="Your contact" />
                    <TextInput type="text" placeholder="contact" value={formData.contact} onChange={handleChange} id="contact" />
                </div>
                <div>
                    <Label value="Your username" />
                    <TextInput type="text" placeholder="Username" value={formData.username} onChange={handleChange} id="username" />
                </div>                
                <div>
                    <Label value="Your password" />
                    <TextInput type="password" placeholder="Password" value={formData.password} onChange={handleChange} id="password" />
                </div>
                <Button gradientDuoTone="purpleToPink" type="submit" disabled={loading}>
                    {
                        loading ? (
                            <>
                            <Spinner size={'sm'} />
                            <span className="pl-3"> Loading...</span>
                            </>                            
                        ) : ( 'Sign Up'

                    )}
                </Button>
            </form>
            <div className="flex gap-2 text-sm mt-5">
                <span> Have an account?</span>
                <Link to={"/sign-in"} className="text-blue-500">
                    Sign in
                </Link>
            </div>            
        </div>
    </div>
  </div>  
}
