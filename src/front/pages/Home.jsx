import { Link, useNavigate } from "react-router-dom";


export const Home = () => {

	const navigate = useNavigate()

	const handleProfile = () => {
		console.log('click')
		//si tenemos el token, lo pasamos a su vista privada, sino que haga login
		localStorage.getItem('token')? navigate('/private') : navigate('/login')
	}


	return (
		<div className="text-center mt-5">
			<h2>Welcome, go to <Link to={'/register'}>Register</Link> if you are new, else <Link to={'/login'}>Login</Link>
			{" "}Or you can go to your <span className="nav nav-link pointer" onClick={handleProfile}>Profile!</span>
			</h2>

		</div>
	);
}; 