import React from "react";
import FilterForm from "../components/Filters";
import FullFeaturedCrudGrid from "../components/Datagrid";
import { getPessoasRequest } from "../services/http/Pessoa";
import { iPessoa } from "../services/http/Types";

const Pessoas = () => {
  const [pessoas, setPessoas] = React.useState<iPessoa[]>([]);

  const onSearch = async (filters: Record<string, unknown>) => {
    const pessoasResult = await getPessoasRequest(filters);
    setPessoas(pessoasResult);
  };

  return (
    <>
      <h1>Controle de Pessoas</h1>
      <FilterForm onSearch={onSearch} />
      <FullFeaturedCrudGrid pessoas={pessoas} />
    </>
  );
};

export default Pessoas;
