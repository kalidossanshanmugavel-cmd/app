import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    Button,
    Container,
    TextField,
    Typography
} from "@mui/material";

import { login } from "../services/authService";
import { useAuth } from "../context/AuthContext";

function Login() {

    const navigate = useNavigate();

    const { checkAuth } = useAuth();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    async function handleLogin(e) {

        e.preventDefault();

        try {

            await login(username, password);

            await checkAuth();

            navigate("/dashboard");

        }

        catch (err) {

            alert("Invalid username/password");

            console.log(err);

        }

    }

    return (

        <Container maxWidth="sm">

            <Typography
                variant="h4"
                mt={5}
                mb={3}
            >

                Login

            </Typography>

            <form onSubmit={handleLogin}>

                <TextField
                    fullWidth
                    label="Username"
                    margin="normal"
                    value={username}
                    onChange={(e) =>
                        setUsername(e.target.value)
                    }
                />

                <TextField
                    fullWidth
                    label="Password"
                    type="password"
                    margin="normal"
                    value={password}
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                />

                <Button
                    fullWidth
                    variant="contained"
                    type="submit"
                    sx={{ mt: 2 }}
                >

                    Login

                </Button>

            </form>

        </Container>

    );

}

export default Login;