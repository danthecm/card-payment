export const formatDate = (input) => {
  const date = new Date(input);
  const month = date.getMonth() + 1;
  const year = date.getFullYear();
  var formattedValue = month + "/" + year;
  return formattedValue;
};
