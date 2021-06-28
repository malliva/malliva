module.exports = {
  displayName: 'market-app-dashboard-dashboard-menu',
  preset: '../../../../jest.preset.js',
  transform: {
    '^.+\\.[tj]sx?$': 'babel-jest',
  },
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  coverageDirectory:
    '../../../../coverage/libs/market-app/dashboard/dashboard-menu',
};
