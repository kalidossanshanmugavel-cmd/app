import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import StudentForm from "../components/StudentForm";

import {
    Typography,
    Paper,
    Button,
    Stack
} from "@mui/material";

import { DataGrid } from "@mui/x-data-grid";

import {
    getStudents,
    createStudent
} from "../services/studentService";

function Students() {

    const [students, setStudents] = useState([]);

    const [open, setOpen] = useState(false);

    const [selectedStudent, setSelectedStudent] = useState(null);

    useEffect(() => {

        loadStudents();

    }, []);

    async function loadStudents() {

        try {

            const data = await getStudents();

            setStudents(data);

        }
        catch (err) {

            console.log(err);

        }

    }

    function openDialog() {

        setSelectedStudent(null);

        setOpen(true);

    }

    function closeDialog() {

        setOpen(false);

    }

    async function saveStudent(student) {

        try {

            await createStudent(student);

            closeDialog();

            loadStudents();

            alert("Student Added Successfully");

        }
        catch (err) {

            console.log(err);

            alert("Unable to Save Student");

        }

    }

const columns = [

    {
        field: "id",
        headerName: "ID",
        width: 80
    },

    {
        field: "name",
        headerName: "Name",
        flex: 1
    },

    {
        field: "age",
        headerName: "Age",
        width: 100
    },

    {
        field: "email",
        headerName: "Email",
        flex: 1
    },

    {
        field: "department",
        headerName: "Department",
        flex: 1
    }

];

    return (

        <DashboardLayout>

            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
                mb={3}
            >

                <Typography variant="h4">

                    Students

                </Typography>

                <Button
                    variant="contained"
                    onClick={openDialog}
                >

                    Add Student

                </Button>

            </Stack>

            <Paper
                elevation={3}
                sx={{
                    height: 500,
                    p: 2
                }}
            >

                <DataGrid
                    rows={students}
                    columns={columns}
                    pageSizeOptions={[5, 10, 20]}
                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 5
                            }
                        }
                    }}
                />

            </Paper>

            <StudentForm
                open={open}
                handleClose={closeDialog}
                handleSave={saveStudent}
                student={selectedStudent}
            />

        </DashboardLayout>

    );

}

export default Students;