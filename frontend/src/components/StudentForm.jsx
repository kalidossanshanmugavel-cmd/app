import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField,
    Button
} from "@mui/material";
import { useEffect, useState } from "react";

function StudentForm({
    open,
    handleClose,
    handleSave,
    student
}) {

    const [form, setForm] = useState({
        name: "",
        age: "",
        email: "",
        department: ""
    });

    useEffect(() => {

        if (student) {
            setForm(student);
        } else {
            setForm({
                name: "",
                age: "",
                email: "",
                department: ""
            });
        }

    }, [student]);

    function handleChange(e) {

        setForm({
            ...form,
            [e.target.name]: e.target.value
        });

    }

    return (

        <Dialog
            open={open}
            onClose={handleClose}
            fullWidth
            maxWidth="sm"
        >

            <DialogTitle>
                {student ? "Edit Student" : "Add Student"}
            </DialogTitle>

            <DialogContent>

                <TextField
                    fullWidth
                    margin="normal"
                    label="Name"
                    name="name"
                    value={form.name}
                    onChange={handleChange}
                />

                <TextField
                    fullWidth
                    margin="normal"
                    label="Age"
                    name="age"
                    type="number"
                    value={form.age}
                    onChange={handleChange}
                />

                <TextField
                    fullWidth
                    margin="normal"
                    label="Email"
                    name="email"
                    value={form.email}
                    onChange={handleChange}
                />

                <TextField
                    fullWidth
                    margin="normal"
                    label="Department"
                    name="department"
                    value={form.department}
                    onChange={handleChange}
                />

            </DialogContent>

            <DialogActions>

                <Button onClick={handleClose}>
                    Cancel
                </Button>

                <Button
                    variant="contained"
                    onClick={() => handleSave(form)}
                >
                    Save
                </Button>

            </DialogActions>

        </Dialog>

    );

}

export default StudentForm;