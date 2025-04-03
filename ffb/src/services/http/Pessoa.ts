import axios from "axios";
import { get_env } from "../../config";
import { iPessoa, iPessoaSnakeCase } from "./Types";

const BASE_URL = get_env().API_URL || "http://127.0.0.1:8000/api";
const PATH = "pessoa";

export const getPessoasRequest = async (filters: {
  nome?: string;
  dataNascimento?: string;
  cpf?: string;
  altura?: number;
  peso?: number;
  sexo?: string;
}) => {
  try {
    const filtersSnakeCase = {
      nome: filters.nome,
      data_nasc: filters.dataNascimento,
      cpf: filters.cpf,
      altura: filters.altura,
      peso: filters.peso,
      sexo: filters.sexo,
    };
    const queryParams = new URLSearchParams(
      filtersSnakeCase as unknown as Record<string, string>
    );
    const queryString = queryParams.toString();
    const { data } = await axios.get(`${BASE_URL}/${PATH}/?${queryString}`);

    const pessoas: iPessoa[] = data.pessoas.map((pessoa: iPessoaSnakeCase) => {
      const dataNascimento = new Date(pessoa.data_nasc);
      const adjustedDataNascimento = new Date(
        dataNascimento.getTime() + dataNascimento.getTimezoneOffset() * 60000
      );
      return {
        id: pessoa.id,
        nome: pessoa.nome,
        dataNascimento: adjustedDataNascimento,
        cpf: pessoa.cpf,
        altura: pessoa.altura,
        peso: pessoa.peso,
        sexo: pessoa.sexo,
      };
    });
    return pessoas;
  } catch (error) {
    console.error("Erro ao buscar pessoas:", error);
    throw error;
  }
};

export const createPessoaRequest = async (payload: iPessoa) => {
  try {
    const body = {
      nome: payload.nome,
      data_nasc: payload.dataNascimento.toISOString().split("T")[0],
      cpf: payload.cpf,
      altura: payload.altura,
      peso: payload.peso,
      sexo: payload.sexo,
    };
    const { data } = await axios.post(`${BASE_URL}/${PATH}/`, body);
    const { pessoa } = data;
    const pessoaUpdated: iPessoa = {
      id: pessoa.id,
      nome: pessoa.nome,
      dataNascimento: new Date(pessoa.data_nasc),
      cpf: pessoa.cpf,
      altura: pessoa.altura,
      peso: pessoa.peso,
      sexo: pessoa.sexo,
    };
    return pessoaUpdated;
  } catch (error) {
    console.error("Erro ao buscar pessoas:", error);
    throw error;
  }
};

export const updatePessoaRequest = async (payload: iPessoa) => {
  try {
    const body = {
      nome: payload.nome,
      data_nasc: payload.dataNascimento.toISOString().split("T")[0],
      cpf: payload.cpf,
      altura: payload.altura,
      peso: payload.peso,
      sexo: payload.sexo,
    };
    const { data } = await axios.put(
      `${BASE_URL}/${PATH}/${payload.id}/`,
      body
    );
    const { pessoa } = data;
    const pessoaUpdated: iPessoa = {
      id: pessoa.id,
      nome: pessoa.nome,
      dataNascimento: new Date(pessoa.data_nasc),
      cpf: pessoa.cpf,
      altura: pessoa.altura,
      peso: pessoa.peso,
      sexo: pessoa.sexo,
    };
    return pessoaUpdated;
  } catch (error) {
    console.error("Erro ao buscar pessoas:", error);
    throw error;
  }
};

export const deletePessoaRequest = async (id: number) => {
  try {
    await axios.delete(`${BASE_URL}/${PATH}/${id}/`);
  } catch (error) {
    console.error("Erro ao buscar pessoas:", error);
    throw error;
  }
};
