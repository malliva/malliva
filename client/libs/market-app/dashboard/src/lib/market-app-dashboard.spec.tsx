import { render } from '@testing-library/react';

import MarketAppDashboard from './market-app-dashboard';

describe('MarketAppDashboard', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppDashboard />);
    expect(baseElement).toBeTruthy();
  });
});
