function numberOfEmployeesWhoMetTarget(
  hours: number[],
  target: number
): number {
  return hours.filter((hour) => hour >= target).length;
}
