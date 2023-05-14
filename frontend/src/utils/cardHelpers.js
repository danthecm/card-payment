export const formatCardNumber = (input) => {
  const newCardNumber = input.replace(/\D/g, "");
  return newCardNumber.replace(/(\d{4})(?=\d)/g, "$1 ");
};

export const removeSpaces = (input) => {
  return input.replace(/\s/g, "");
};
