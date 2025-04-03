import React from "react";
import { useForm, Controller } from "react-hook-form";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import MenuItem from "@mui/material/MenuItem";

interface FilterFormProps {
  onSearch: (filters: Record<string, unknown>) => void;
}

const FilterForm: React.FC<FilterFormProps> = ({ onSearch }) => {
  const { handleSubmit, control, reset } = useForm({
    defaultValues: {
      nome: "",
      cpf: "",
      sexo: "",
      dataNascimento: "",
      peso: "",
      altura: "",
    },
  });

  const onSubmit = (data: Record<string, unknown>) => {
    onSearch(data);
  };

  const handleReset = () => {
    reset();
    onSearch({});
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit(onSubmit)}
      sx={{
        display: "flex",
        flexDirection: "row",
        gap: 1,
        alignItems: "center",
        marginBottom: 2,
      }}
    >
      <Controller
        name="nome"
        control={control}
        render={({ field }) => (
          <TextField {...field} label="Nome" variant="outlined" size="small" />
        )}
      />
      <Controller
        name="cpf"
        control={control}
        render={({ field }) => (
          <TextField {...field} label="CPF" variant="outlined" size="small" />
        )}
      />
      <Controller
        name="sexo"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            variant="outlined"
            select
            label="Sexo"
            size="small"
            sx={{ width: 200 }}
          >
            <MenuItem value="M">Masculino</MenuItem>
            <MenuItem value="F">Feminino</MenuItem>
          </TextField>
        )}
      />
      <Controller
        name="dataNascimento"
        control={control}
        render={({ field }) => (
          <TextField {...field} type="date" variant="outlined" size="small" />
        )}
      />
      <Controller
        name="altura"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            label="Altura"
            variant="outlined"
            size="small"
            sx={{ width: 100 }}
          />
        )}
      />
      <Controller
        name="peso"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            label="Peso"
            variant="outlined"
            size="small"
            sx={{ width: 100 }}
          />
        )}
      />
      <Button type="submit" variant="contained" color="primary">
        Buscar
      </Button>
      <Button
        type="button"
        variant="outlined"
        color="secondary"
        onClick={handleReset}
      >
        Limpar
      </Button>
    </Box>
  );
};

export default FilterForm;
