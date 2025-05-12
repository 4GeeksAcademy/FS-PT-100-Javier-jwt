import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { Register } from "../components/register.jsx";
import { Login } from "../components/login.jsx";
import { Private } from "../components/private.jsx";
import userServices from "../services/userServices.js";

export const Home = () => {

	const { store, dispatch } = useGlobalReducer()



	const handleClick = () => {
		console.log('asdasdasd');
		
		userServices.getUserInfo().then(data => dispatch({type: 'get_user_info', payload: data})
		)
	}



	return (
		<div className="text-center mt-5">
			<h2>first register or login</h2>
			<Register />

			<Login />
			<h2>then</h2>
			<button onClick={handleClick}> Get your info after login/registering</button>

			{/* si tengo info en store.user, muestra private */}
			{localStorage.getItem('token') && <Private />}

		</div>
	);
}; 