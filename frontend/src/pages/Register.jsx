import { Container, Paper, Typography } from "@mui/material";

function Register() {
  return (
    <Container maxWidth="sm" sx={{ mt: 8 }}>
      <Paper elevation={4} sx={{ p: 4 }}>
        <Typography variant="h4">
          Register
        </Typography>
      </Paper>
    </Container>
  );
}

export default Register;