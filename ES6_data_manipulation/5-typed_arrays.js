export default function createInt8TypedArray(length, position, value) {
  const result = new DataView(new ArrayBuffer(length));
  result.setInt8(position, value);
  return result;
}
