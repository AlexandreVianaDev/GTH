export const get_env = () => {
  const env = import.meta.env;
  return {
    API_URL: env.API_URL,
  };
};
